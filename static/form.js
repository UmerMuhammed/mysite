function toggleFields() {
    var type = document.getElementById("selectionType").value;
    var orderFormsContainer = document.getElementById("orderFormsContainer");
    var contactInfoContainer = document.getElementById("contactInfoContainer");

    if (type === "Order Submit") {
        orderFormsContainer.style.display = "block";
        contactInfoContainer.style.display = "none";
    } else if (type === "Visit only") {
        orderFormsContainer.style.display = "none";
        contactInfoContainer.style.display = "none";
    } else {
        orderFormsContainer.style.display = "none";
        contactInfoContainer.style.display = "none";
    }
}