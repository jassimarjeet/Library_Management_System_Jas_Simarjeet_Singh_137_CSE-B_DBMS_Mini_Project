from graphviz import Digraph

diagram = Digraph(format='png', engine='dot')
diagram.attr(rankdir='TB', size='10,10')


# Books Entity
diagram.node("Books", "Books", shape="rectangle")
diagram.node("Book_ID", "Book_ID (PK)", shape="ellipse")
diagram.node("Title", "Title", shape="ellipse")
diagram.node("Author", "Author", shape="ellipse")
diagram.node("Publisher", "Publisher", shape="ellipse")
diagram.node("ISBN", "ISBN", shape="ellipse")
diagram.node("Category", "Category", shape="ellipse")
diagram.node("Copies_Available", "Copies_Available", shape="ellipse")

# Connect attributes to Books
diagram.edge("Books", "Book_ID")
diagram.edge("Books", "Title")
diagram.edge("Books", "Author")
diagram.edge("Books", "Publisher")
diagram.edge("Books", "ISBN")
diagram.edge("Books", "Category")
diagram.edge("Books", "Copies_Available")

# Users Entity
diagram.node("Users", "Users", shape="rectangle")
diagram.node("User_ID", "User_ID (PK)", shape="ellipse")
diagram.node("Name", "Name", shape="ellipse")
diagram.node("Email", "Email", shape="ellipse")
diagram.node("Phone", "Phone", shape="ellipse")
diagram.node("Address", "Address", shape="ellipse")
diagram.node("Role", "Role", shape="ellipse")

# Connect attributes to Users
diagram.edge("Users", "User_ID")
diagram.edge("Users", "Name")
diagram.edge("Users", "Email")
diagram.edge("Users", "Phone")
diagram.edge("Users", "Address")
diagram.edge("Users", "Role")

# Admins Entity
diagram.node("Admins", "Admins", shape="rectangle")
diagram.node("Admin_ID", "Admin_ID (PK)", shape="ellipse")
diagram.node("Admin_Name", "Name", shape="ellipse")
diagram.node("Admin_Email", "Email", shape="ellipse")
diagram.node("Admin_Phone", "Phone", shape="ellipse")
diagram.node("Admin_Address", "Address", shape="ellipse")

# Connect attributes to Admins
diagram.edge("Admins", "Admin_ID")
diagram.edge("Admins", "Admin_Name")
diagram.edge("Admins", "Admin_Email")
diagram.edge("Admins", "Admin_Phone")
diagram.edge("Admins", "Admin_Address")

# Borrowing Entity
diagram.node("Borrowing", "Borrowing", shape="rectangle")
diagram.node("Borrow_ID", "Borrow_ID (PK)", shape="ellipse")
diagram.node("Borrow_Book_ID", "Book_ID (FK)", shape="ellipse")
diagram.node("Borrow_User_ID", "User_ID (FK)", shape="ellipse")
diagram.node("Issue_Date", "Issue_Date", shape="ellipse")
diagram.node("Due_Date", "Due_Date", shape="ellipse")
diagram.node("Return_Date", "Return_Date", shape="ellipse")

# Connect attributes to Borrowing
diagram.edge("Borrowing", "Borrow_ID")
diagram.edge("Borrowing", "Borrow_Book_ID")
diagram.edge("Borrowing", "Borrow_User_ID")
diagram.edge("Borrowing", "Issue_Date")
diagram.edge("Borrowing", "Due_Date")
diagram.edge("Borrowing", "Return_Date")

# Feedback Entity
diagram.node("Feedback", "Feedback", shape="rectangle")
diagram.node("Feedback_ID", "Feedback_ID (PK)", shape="ellipse")
diagram.node("Feedback_User_ID", "User_ID (FK)", shape="ellipse")
diagram.node("Feedback_Text", "Feedback_Text", shape="ellipse")
diagram.node("Rating", "Rating", shape="ellipse")

# Connect attributes to Feedback
diagram.edge("Feedback", "Feedback_ID")
diagram.edge("Feedback", "Feedback_User_ID")
diagram.edge("Feedback", "Feedback_Text")
diagram.edge("Feedback", "Rating")

# Add Relationships
diagram.node("Initiates", "Initiates", shape="diamond")
diagram.edge("Users", "Initiates")
diagram.edge("Initiates", "Borrowing")

diagram.node("Referenced_by", "Referenced_by", shape="diamond")
diagram.edge("Books", "Referenced_by")
diagram.edge("Referenced_by", "Borrowing")

diagram.node("Gives", "Gives", shape="diamond")
diagram.edge("Users", "Gives")
diagram.edge("Gives", "Feedback")

# Render and save the diagram
output_path_styled = "Library_ER_Diagram_Styled_v2"
diagram.render(output_path_styled, format='png', cleanup=True)

print(output_path_styled + ".png")