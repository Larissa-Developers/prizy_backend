from django.test import TestCase, override_settings
from unittest import skip
from unittest.mock import patch

from meetupws.service import MeetupService


class MeetupServiceTest(TestCase):
    """
    Test suite for the moodlews package
    """

    @override_settings(MEETUPCOM_OAUTH_TOKEN="token")
    @patch("meetup.api.Client", autospec=True)
    def setUp(self, mock) -> None:
        """
        Runs before every test method

        :return: None
        """

        self.service = MeetupService()

    def tearDown(self) -> None:
        """
        Runs after every test method

        :return:
        """

        self.service = None

    def test_create_request_config(self) -> None:
        """
        Test creating a Meetup.com API request configuration
        No optional parameters are provided

        :return: None
        """

        config = self.service._create_request_config({'urlname': 'name'})
        self.assertEqual(config, {'urlname': 'name'})

    def test_create_request_config_with_optional_params(self) -> None:
        """
        Test creating a Meetup.com API request configuration
        Optional parameters are provided

        :return: None
        """

        config = self.service._create_request_config({'urlname': 'name'}, {'fields': ['a', 'b'], 'timezone': 'UTC'})
        self.assertEqual(config, {'urlname': 'name', 'fields': ['a', 'b'], 'timezone': 'UTC'})

    @skip
    def test_get_meetup_group(self) -> None:
        """
        Test GET https://api.meetup.com/:urlname?params

        :return: None
        """

    @skip
    def test_get_meetup_events(self) -> None:
        """
        Test GET https://api.meetup.com/:urlname/events?params

        :return: None
        """
