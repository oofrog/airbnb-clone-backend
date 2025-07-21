from rest_framework.test import APITestCase
from .. import models


class TestAmenities(APITestCase):

    NAME = "TEST"
    DESC = "testing"
    URL = "/api/v1/rooms/amenities/"

    def setUp(self):

        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_all_amenities(self):

        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "not 200",
        )
        self.assertIsInstance(
            data,
            list,
        )
        self.assertEqual(
            len(data),
            1,
        )
        self.assertEqual(
            data[0]["name"],
            self.NAME,
        )
        self.assertEqual(
            data[0]["description"],
            self.DESC,
        )

    def test_create_amenity(self):

        new_amenity_name = "NEW Amenity"
        new_amenity_desciption = "new DESC"

        response = self.client.post(
            self.URL,
            data={
                "name": new_amenity_name,
                "description": new_amenity_desciption,
            },
        )
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "NOT 200",
        )

        self.assertEqual(
            data["name"],
            new_amenity_name,
        )
        self.assertEqual(
            data["description"],
            new_amenity_desciption,
        )

        response = self.client.post(self.URL)
        data = response.json()

        self.assertEqual(
            response.status_code,
            400,
        )
        self.assertIn(
            "name",
            data,
        )
        