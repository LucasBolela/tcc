from rest_framework.test import APITestCase
from django.test.client import MULTIPART_CONTENT, encode_multipart, BOUNDARY
from django.core.files.base import ContentFile


class ReaderTest(APITestCase):
    def test_reader_file_uploaded_success(self):
        document = ContentFile(b"foo", "test.png")
        url = "/api/reader/"
        response = self.client.post(
            path=url,
            data=encode_multipart(data=dict(file=document), boundary=BOUNDARY),
            content_type=MULTIPART_CONTENT,
        )

        self.assertEqual(200, response.status_code)

    def test_reader_empty_data_failed(self):
        url = "/api/reader/"
        response = self.client.post(
            path=url,
            data=encode_multipart(data=dict(), boundary=BOUNDARY),
            content_type=MULTIPART_CONTENT,
        )

        self.assertEqual(422, response.status_code)
        self.assertEqual(
            "Campos 'link' e file' não enviados.", response.data["message"]
        )
