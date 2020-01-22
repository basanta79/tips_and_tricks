# For more information about cookies:
# https://api.rubyonrails.org/v5.1.7/classes/ActionDispatch/Cookies.html

# Sets a simple session cookie.
# This cookie will be deleted when the user's browser is closed.
cookies[:user_name] = "david"

# Cookie values are String based. Other data types need to be serialized.
cookies[:lat_lon] = JSON.generate([47.68, -122.37])

# Sets a cookie that expires in 1 hour.
cookies[:login] = { value: "XJ-122", expires: 1.hour.from_now }

# Sets a signed cookie, which prevents users from tampering with its value.
# The cookie is signed by your app's `secrets.secret_key_base` value.
# It can be read using the signed method `cookies.signed[:name]`
cookies.signed[:user_id] = current_user.id

# Sets an encrypted cookie value before sending it to the client which
# prevent users from reading and tampering with its value.
# The cookie is signed by your app's `secrets.secret_key_base` value.
# It can be read using the encrypted method `cookies.encrypted[:name]`
cookies.encrypted[:discount] = 45

# Sets a "permanent" cookie (which expires in 20 years from now).
cookies.permanent[:login] = "XJ-122"

# You can also chain these methods:
cookies.permanent.signed[:login] = "XJ-122"

######################################################
# Examples of reading
######################################################

cookies[:user_name]           # => "david"
cookies.size                  # => 2
JSON.parse(cookies[:lat_lon]) # => [47.68, -122.37]
cookies.signed[:login]        # => "XJ-122"
cookies.encrypted[:discount]  # => 45


######################################################
# Examples of deleting
######################################################

cookies.delete :user_name


# Please note that if you specify a :domain when setting a cookie, you must also specify the domain when deleting the cookie:

cookies[:name] = {
  value: 'a yummy cookie',
  expires: 1.year.from_now,
  domain: 'domain.com'
}

cookies.delete(:name, domain: 'domain.com')

#
# The option symbols for setting cookies are:
# 
# :value - The cookie's value.
# 
# :path - The path for which this cookie applies. Defaults to the root of the application.
# 
# :domain - The domain for which this cookie applies so you can restrict to the domain level. If you use a schema like www.example.com and want to share session with user.example.com set :domain to :all. Make sure to specify the :domain option with :all or Array again when deleting cookies.
# 
# domain: nil  # Does not set cookie domain. (default)
# domain: :all # Allow the cookie for the top most level
#              # domain and subdomains.
# domain: %w(.example.com .example.org) # Allow the cookie
#                                       # for concrete domain names.
# :tld_length - When using :domain => :all, this option can be used to explicitly set the TLD length when using a short (<= 3 character) domain that is being interpreted as part of a TLD. For example, to share cookies between user1.lvh.me and user2.lvh.me, set :tld_length to 1.
# 
# :expires - The time at which this cookie expires, as a Time object.
# 
# :secure - Whether this cookie is only transmitted to HTTPS servers. Default is false.
# 
# :httponly - Whether this cookie is accessible via scripting or only HTTP. Defaults to false.

