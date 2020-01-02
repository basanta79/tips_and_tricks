# Convert string to symbol

## If string has no spaces
dict = {"string_word".to_sym => "using .to_sym", :other => "other"}
puts dict[:string_word]

## If string has spaces
dict = {"string word".gsub(/\s+/,"_").downcase.to_sym => "with spaces", :other => "other"}
puts dict[:string_word]

## If using rails
# dict = {"string word".parameterize.underscore.to_sym => "using rails", :other => "other"}
# puts dict[:string_word]

## using semicolon (no spaces allowed)
dict = {:"string_word" => "with semicolon"}
puts dict[:string_word]
