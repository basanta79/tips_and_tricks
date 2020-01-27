
|  | nil? | empty? | blank? | present? |
| - | - | - | - | - |  
| nil | true | noMethodError | true | false |
| false | false | NoMethodError | true | false |
| true | false | NoMethodError | false | true |
| "" | false | true | true | false |
| " " | false | false | true | false |
| [] | false | true | true | false |
| {} | false | true | true | false |
| "Hello" | false | false | false | true |
| 25 | false | UndefinedMethod | false | true |