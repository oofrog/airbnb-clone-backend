from rest_framework.test import APITestCase
from .. import models


class TestAmenity(APITestCase):

    NAME = "TEST AMENity"
    DESC = "TESt DESc"
    URL = "/api/v1/amenities/1"

    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_amenity_not_found(self):
        response = self.client.get("/api/v1/rooms/amenities/2")
        self.assertEqual(
            response.status_code,
            404,
        )

    def test_get_amenity(self):
        response = self.client.get("/api/v1/rooms/amenities/1")
        self.assertEqual(
            response.status_code,
            200,
        )

        data = response.json()
        self.assertEqual(
            data["name"],
            self.NAME,
        )
        self.assertEqual(
            data["description"],
            self.DESC,
        )

    def test_put_amenity(self):

        updated_name = "UPDATED NAME"
        updated_desc = "UPDATED DESC"

        response = self.client.put(
            "/api/v1/rooms/amenities/1",
            data={
                "name": updated_name,
                "description": updated_desc,
            },
        )
        data = response.json()
        self.assertEqual(
            response.status_code,
            200,
        )
        self.assertEqual(
            data["name"],
            updated_name,
        )
        self.assertEqual(
            data["description"],
            updated_desc,
        )

        long_name = "a" * 200
        response = self.client.put(
            "/api/v1/rooms/amenities/1",
            data={
                "name": long_name,
            },
        )
        self.assertEqual(
            response.status_code,
            400,
        )

    def test_delete_amenity(self):
        response = self.client.delete("/api/v1/rooms/amenities/1")
        self.assertEqual(
            response.status_code,
            204,
        )
