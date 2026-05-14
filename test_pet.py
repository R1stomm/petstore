import pytest
import requests


class TestPetStoreVariant8:
    pet_id = None  

    def test_01_create_pet(self, base_url, pet_data):
        """POST /pet — создать нового питомца"""
        response = requests.post(f"{base_url}/pet", json=pet_data)
        assert response.status_code == 200
        json_data = response.json()
        assert json_data["name"] == pet_data["name"]
        assert json_data["status"] == pet_data["status"]
       
        TestPetStoreVariant8.pet_id = json_data["id"]
        print(f"\nCreated pet with ID: {TestPetStoreVariant8.pet_id}")

    def test_02_get_pet_by_id(self, base_url, pet_data):
        """GET /pet/{petId} — получить питомца по ID"""
       
        if TestPetStoreVariant8.pet_id is None:
            pytest.skip("Pet not created yet, run test_01_create_pet first")
        
        response = requests.get(f"{base_url}/pet/{TestPetStoreVariant8.pet_id}")
        assert response.status_code == 200
        json_data = response.json()
        assert json_data["id"] == TestPetStoreVariant8.pet_id
        assert json_data["name"] == pet_data["name"]
        print(f"\nGot pet with ID: {TestPetStoreVariant8.pet_id}")

    def test_03_upload_image(self, base_url, pet_data):
        """POST /pet/{petId}/uploadImage — загрузить изображение"""
        if TestPetStoreVariant8.pet_id is None:
            pytest.skip("Pet not created yet, run test_01_create_pet first")
        
        files = {"file": ("rex.jpg", b"fake image content", "image/jpeg")}
        data = {"additionalMetadata": "test upload"}
        response = requests.post(
            f"{base_url}/pet/{TestPetStoreVariant8.pet_id}/uploadImage",
            files=files,
            data=data
        )
        assert response.status_code == 200
        json_data = response.json()
        assert json_data["code"] == 200
        assert "Uploaded" in json_data["message"] or "rex.jpg" in json_data["message"]
        print(f"\nUploaded image for pet ID: {TestPetStoreVariant8.pet_id}")

    def test_04_cleanup(self, base_url):
        
        if TestPetStoreVariant8.pet_id and TestPetStoreVariant8.pet_id != 0:
            response = requests.delete(f"{base_url}/pet/{TestPetStoreVariant8.pet_id}")
            assert response.status_code == 200
            print(f"\nDeleted pet with ID: {TestPetStoreVariant8.pet_id}")
