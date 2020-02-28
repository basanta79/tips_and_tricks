

array = ["hola", 1, 5.6, 2..5]

# Loop for each item
array.each do |item|
    puts "el item es: #{item}" #[item]
end

# Add new element
array << "pablo"
puts array

# reverse an array
puts "###############################################"
puts "is posisble to reverse an array using .reverse!"
puts "###############################################"
puts array.reverse!

arr = nil
if (arr && arr.length>1)
    puts('@@@@@@@@@@@@@@')
else
    puts('$$$$$$$$$$$$$')
end

# Check Item in the array
puts array.include?("hola")
puts array.include?("mundo")

# Check all methods 
# puts array.methods
