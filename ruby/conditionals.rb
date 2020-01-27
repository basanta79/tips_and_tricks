a = 5

if a < 5
    puts "menor que 5"
elsif a == 5
    puts "igual a 5"
else
    puts "mayor que 5"
end


mes = 2

case mes
when 1 then
    puts "Enero"
when (2..4)
    puts "Feb, mar, abr"
when (5...13)
    puts "otro mes"
else
    puts "mes inexistente"
end

str = ""

# This only exists in Rails, not Ruby
# if str.blank
#     puts('string vacio')
# end

str = nil

str.nil? 
    puts('string a nil')

