require 'nokogiri'
require 'HTTParty'
require 'pry'



page = HTTParty.get('https://www.vodafone.es/c/particulares/es/acceso-area-privada/?service=https%3a%2f%2fwww.vodafone.es%2fc%2fmivodafone%2fes%2farea-privada-contrato%2f')

parsed_page = Nokogiri::HTML(page)

username = parsed_page.search('input[id="userid"]')
password = parsed_page.search('input[id="password"]')

puts(username)
puts(password)

# puts(parsed_page.search('input[type="text"]'))

# pry.start(binding)

