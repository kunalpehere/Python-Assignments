# 6. Create a string vehicle_no = "MH12AB1234". 
# Using startswith(), check whether the vehicle is registered in Maharashtra ("MH"). 
# Then create a string file_name = "report_final.pdf" and 
# use endswith() to check whether it is a PDF file.

vehicle_no = "MH12AB1234"
file_name = "report_final.pdf"

is_maharashtra = vehicle_no.startswith("MH")
is_pdf = file_name.endswith(".pdf")

print(f"Vehicle {vehicle_no} registered in MH: {is_maharashtra}")
print(f"File {file_name} is a PDF: {is_pdf}")