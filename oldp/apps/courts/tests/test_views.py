from django.test import LiveServerTestCase, tag
from django.urls import reverse


@tag('views')
class CourtsViewsTestCase(LiveServerTestCase):
    fixtures = [
        'locations/countries.json', 'locations/states.json', 'locations/cities.json',
        'courts/courts.json',
    ]

    def test_index(self):
        res = self.client.get(reverse('courts:index'))

        self.assertContains(res, 'Amtsgericht Aalen')
        self.assertContains(res, 'EuGH')
        self.assertContains(res, 'Unknown state')

    def test_index_state(self):
        res = self.client.get(reverse('courts:index_state', args=('unknown-state', )))

        self.assertNotContains(res, 'Amtsgericht Aalen')
        self.assertContains(res, 'EuGH')
        self.assertContains(res, 'Unknown court')

    def test_detail(self):
        res = self.client.get(reverse('courts:detail', args=('ag-aalen',)))

        self.assertContains(res, 'Amtsgericht Aalen')
        self.assertContains(res, 'AGAALEN')

        # TODO test for cases
