domestic_cat={"siamese cat","british shorthair","maine coon","persian cat","ragdoll"}

domestic_dog={"german shepherd","bulldog","labrador retriever", "golden retriever"}

wild_dog={"wolf hybird","great dane","doberman pinscher","siberian husky","malamute alaskan"}

endengred_animalls={"scottish deerhound","otterhound","maine coon","siamese cat","golden retriever","great dane"}

pets=domestic_cat|domestic_dog#union

dogs=domestic_dog|wild_dog#union

endangred_dogs=dogs&endengred_animalls#intersection

print("pets:",pets,"\ndogs:",dogs,"\nendangred dogs:",endangred_dogs)

