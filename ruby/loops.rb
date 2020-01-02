
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "junio", "julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

for mes in meses
    puts mes
end

meses.each do |mes|
    puts mes
end

c = 12

while c > 0
    puts meses[c]
    c = c - 1
end

c = 12
 
until c == 0
    puts c
    c = c - 1
end