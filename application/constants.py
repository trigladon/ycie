ASSET_TYPE_CATEGORY_NEWS = "category_news"
ASSET_TYPE_NEWS = "news"

GOVERNMENT_ROLE_MANAGER = 'manager'
GOVERNMENT_ROLE_ADMIN = 'admin'

APARTMENT_ROLE_OWNER = 'owner'
APARTMENT_ROLE_TENANT = 'tenant'
APARTMENT_ROLE_LODGER = 'lodger'

APARTMENT_STATUS_UNDER_CONSIDERATION_GOVERNMENT = 'under consideration government'
APARTMENT_STATUS_UNDER_CONSIDERATION_HOUSE = 'under consideration house'
APARTMENT_STATUS_BLOCKED = 'blocked'
APARTMENT_STATUS_ACCEPTED = 'accepted'

MODEL_ROLES = (
    (APARTMENT_ROLE_TENANT, 'Tenant'),
    (APARTMENT_ROLE_OWNER, 'Owner'),
    (APARTMENT_ROLE_LODGER, 'Lodger'),
)

APARTMENT_STATUS = (
    (APARTMENT_STATUS_UNDER_CONSIDERATION_GOVERNMENT, 'Under consideration in a government'),
    (APARTMENT_STATUS_UNDER_CONSIDERATION_HOUSE, 'Under consideration in a house owner'),
    (APARTMENT_STATUS_BLOCKED, 'Blocked'),
    (APARTMENT_STATUS_BLOCKED, 'Accepted'),
)