class Dog:
    def __init__(self, breed, has_owner, age):
        print("Constructor invoked!")
        self.breed = breed
        self.has_owner = has_owner
        self.age = age

if __name__ == "__main__":
    print("Main method started")
    
    fido = Dog("poodle", False, 4)
    nunzio = Dog("shiba inu", True, 12)
    
    is_fido_older = fido.age > nunzio.age
    total_dog_years = nunzio.age + fido.age
    
    print(f"Two dogs created: a {fido.breed} and a {nunzio.breed}")
    print(f"The statement that Fido is an older dog is: {is_fido_older}")
    print(f"The total age of the dogs is: {total_dog_years}")
    print("Main method finished")
