# Views

The views are stored into app/views folder.

Each controller has its own subfolder inside app/views, so, for instance, users controller will have its main view: ```app/views/users/index.html.erb```

We can reuse other templates, like header, footer, etc.

TIP: Views MUST NOT have logic inside, all information to show must be shown using variables.

To render a view we can use ```render :index``` and this will load the index.htm.erb view inside the specific folder. 
If we don't use render instruction, the controller will render the template with the same name of the method inside the controller.

Is possible to redirect to another view using ```redirect_to```

## Print values from the controller in the template and code
<hr>

**Variable**<br>
<%= @user %>

**Attribute from an object**<br>
<%= @user.name %>

**Code**<br>
<% instructions %>


**Example**<br>
```
<% if user_signed_in? %>
    <div> <%= @user.name %> </div>
<% else %>
    <div> Usuario no identificado <div>
<% end %>
```
```
<% @users.find_each do |user| %>
    <div> Name: <%= user.name %> </div>
<% end %>
```

## Reuse fields in templates
<hr>
The main template is located at ```app/views/layouts/application.html.erb```

**yield**<br>
The reserved word yield is used to place a hole to fill with content from detailed views. Is possible to have more than one yield, the way to differentiate those yields is ``` <%= yield :title %>```

**content_for**<br>
Is possible to set values for placeholders around all views, like yield, the other way is content_for.
For example, in application.html.erb we can put: ```<title><%= content_for?(:title) ? content_for(:title) : "Shift Dashboard" %></title>``` 
And in a view set: ```<%- title " - Transaction" %>```



