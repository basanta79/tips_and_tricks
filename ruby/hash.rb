# Create a hash using symbols as keys
hash = {:name => "Pablo", last_name: "Lopez"}
# Create a hash (less eficient) using strings as keys
hash_2 = {"name" => "Pablo", "last_name" => "Lopez"}


KEY_1 = 'custom_key'
hash_3 = {KEY_1.to_sym => "custom_value_1"}

puts("Access to a value using symbol")
puts hash[:name]
puts("Change the value of the hash using symbol")
hash[:name]="Eva"
puts hash[:name]
puts("Access to a value using symbol created in different way")
puts hash[:last_name]
puts("When hash is created using string you cannot access it using symbol (blank in the output)")
puts hash_2[:name]
puts("You have to use a string")
puts hash_2["name"]

puts hash_3[KEY_1.to_sym]
puts hash_3[:custom_key]
# Check if a key is present in a dictionary
puts hash.has_key?(:name)

