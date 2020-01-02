# Create a hash using symbols as keys
hash = {:name => "Pablo", last_name: "Lopez"}
# Create a hash (less eficient) using strings as keys
hash_2 = {"name" => "Pablo", "last_name" => "Lopez"}


KEY_1 = 'custom_key'
hash_3 = {KEY_1.to_sym => "custom_value_1"}

# Access to a value using symbol
puts hash[:name]
puts hash[:last_name]
# This is not possible (blank in the output)
puts hash_2[:name]
# You have to use:
puts hash_2["name"]

puts hash_3[KEY_1.to_sym]
puts hash_3[:custom_key]
# Check if a key is present in a dictionary
puts hash.has_key?(:name)

