from django.utils.text import slugify
unique_list = {'1':'joel-kinny'}

def get_unique_slug(*slugable_field_name):
    """
    Takes a model instance, sluggable field name (such as 'title') of that
    model as string, slug field name (such as 'slug') of the model as string;
    returns a unique slug as string.
    """
    slugs="-".join(slugable_field_name[0])
    slug=""
    slug += slugify(slugs)
    print(slug)

    unique_slug = slug
    extension = 1
    print("DONE with slugable fields")
    slug_field_name = list(slugable_field_name[1])
    print(slug_field_name)
    for i in range(len(slug_field_name)):
        if unique_slug in slug_field_name:
            unique_slug = '{}-{}'.format(slug, extension)
            print(unique_slug)
            slug_field_name.append(unique_slug)
            extension += 1

print(get_unique_slug(['joel','kinny'],['joel-kinny','joel-kinny-1','joel-kinny-2']))

