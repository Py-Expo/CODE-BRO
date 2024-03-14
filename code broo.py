from roboflow import Roboflow
rf = Roboflow(api_key="d3hU2oVmh3qhVwUSb9UJ")
project = rf.workspace().project("MODEL_ENDPOINT")
model = project.version(1).model

# infer on a local image
print(model.predict("your_image.jpg").json())

# visualize your prediction
# model.predict("your_image.jpg").save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True).json())