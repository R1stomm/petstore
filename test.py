import pytest
import requests


class TestPetStoreVariant8:

    def test_create_pet(self, base_url, pet_data):
        """POST /pet — создать нового питомца"""
        response = requests.post(f"{base_url}/pet", json=pet_data)
        assert response.status_code == 200
        json_data = response.json()
        assert json_data["name"] == pet_data["name"]
        assert json_data["status"] == pet_data["status"]
        # Сохраняем ID для следующих тестов
        pet_data["id"] = json_data["id"]

    def test_get_pet_by_id(self, base_url, pet_data):
        """GET /pet/{petId} — получить питомца по ID"""
        pet_id = pet_data["id"]
        response = requests.get(f"{base_url}/pet/{pet_id}")
        assert response.status_code == 200
        json_data = response.json()
        assert json_data["id"] == pet_id
        assert json_data["name"] == pet_data["name"]

    def test_upload_image(self, base_url, pet_data):
        """POST /pet/{petId}/uploadImage — загрузить изображение"""
        pet_id = pet_data["id"]
        files = {"file": ("rex.jpg", b"fake image content", "image/jpeg")}
        data = {"additionalMetadata": "test upload"}
        response = requests.post(
            f"{base_url}/pet/{pet_id}/uploadImage",
            files=files,
            data=data
        )
        assert response.status_code == 200
        json_data = response.json()
        assert json_data["code"] == 200
        assert "Uploaded" in json_data["message"] or "rex.jpg" in json_data["message"]

    def test_cleanup(self, base_url, pet_data):
        """Удаление питомца после тестов (не обязательно по заданию, но для чистоты)"""
        pet_id = pet_data.get("id")
        if pet_id:
            requests.delete(f"{base_url}/pet/{pet_id}")
