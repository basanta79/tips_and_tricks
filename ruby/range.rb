
# Declare a range including last number
r = (1..10)

# Declare a range excluding last number
r_2 = (1...10)


r.each do |item|
    puts item
end

r_2.each do |item|
    puts item
end
