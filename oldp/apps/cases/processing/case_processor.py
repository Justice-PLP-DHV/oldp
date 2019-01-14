import os
from json import JSONDecodeError

from django.core.exceptions import ValidationError
from django.db import IntegrityError, DataError, OperationalError

from oldp.apps.cases.models import *
from oldp.apps.processing.content_processor import ContentProcessor, InputHandlerFS, InputHandlerDB
from oldp.apps.processing.errors import ProcessingError
from oldp.apps.references.models import CaseReferenceMarker

"""

Build proper processing

1) Refs
    a) build regex extractor
    b) validate (search for §, urteil, ... and check whether ref was detected)

2) Content
    a) Streitwert ...
    b) NER
"""

logger = logging.getLogger(__name__)


class CaseProcessor(ContentProcessor):
    model = Case

    def __init__(self):
        super().__init__()

        self.es_type = 'case'
        self.db_models = [Case, CaseReferenceMarker]
        self.input_path = os.path.join(self.working_dir, 'cases')

    def empty_content(self):
        Case.objects.all().delete()

    def process_content(self):
        for i, content in enumerate(self.pre_processed_content):  # type: Case
            try:
                # First save (some processing steps require ids) TODO is this really useful?
                # content.full_clean()  # Validate model
                content.save()

                self.call_processing_steps(content)

                # Save again
                content.save()

                logger.debug('Completed: %s' % content)

                self.doc_counter += 1
                self.processed_content.append(content)

            except (ValidationError, DataError, OperationalError, IntegrityError, ProcessingError) as e:
                logger.error('Cannot process case: %s; %s' % (content, e))
                self.processing_errors.append(e)
                self.doc_failed_counter += 1


class CaseInputHandlerDB(InputHandlerDB):
    def get_model(self):
        return Case


class CaseInputHandlerFS(InputHandlerFS):
    """Read cases for initial processing from file system"""
    dir_selector = '/*.json'

    def handle_input(self, input_content):
        try:
            logger.debug('Reading case JSON from %s' % input_content)

            case = Case.from_json_file(input_content)
            case.source_path = input_content

            self.pre_processed_content.append(case)

        except JSONDecodeError:
            raise ProcessingError('Cannot parse JSON from %s' % input_content)


if __name__ == '__main__':
    print('Do not call CaseProcessor directly. Run django command: ./manage.py process_cases')
