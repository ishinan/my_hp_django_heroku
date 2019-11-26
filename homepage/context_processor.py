from homepage import settings

# The context processor function
def get_nav_links(request):
    nav_links = settings.DATA_NAV_LIST
    print(f"NAV: {nav_links}")
    return {
        'navlinks': nav_links,
    }