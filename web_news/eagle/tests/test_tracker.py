from django.test import TestCase, Client


class TrackerTest(TestCase):
    def test_tracker_post(self):
        requests_client = Client()
        endpoint = "/api/tracker/"
        response = requests_client.post(
            endpoint,
            data={"task": "Teste dos amigos 201"},
            content_type="application/json",
        )

        assert response.status_code == 201
        assert response.data["task"] == "Teste dos amigos 201"

    def test_tracker_get(self):
        requests_client = Client()
        endpoint = "/api/tracker/"
        requests_client.post(
            endpoint,
            data={"task": "Teste dos amigos 201"},
            content_type="application/json",
        )

        response = requests_client.get(endpoint)

        assert response.status_code == 200
        assert response.data[0]["task"] == "Teste dos amigos 201"
