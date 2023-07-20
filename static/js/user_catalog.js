

let clickedCategory=document.querySelectorAll(".cat-btn");
clickedCategory.forEach(function (button) {
    button.addEventListener("click", function () {
        clickedCategory.forEach(function (btn) {
            btn.classList.remove("clickedCategoryStyle");
        });

        button.classList.toggle("clickedCategoryStyle")
    });
  });

document.querySelectorAll(".minus").forEach((button) => {
    button.addEventListener("click", decreaseQuantity);
});

document.querySelectorAll(".plus").forEach((button) => {
    button.addEventListener("click", increaseQuantity);
});
function decreaseQuantity(){
    let itemQuantity = this.parentNode.querySelector(".qunty");
    let quantity = parseInt(itemQuantity.innerHTML);
    if (quantity > 0) {
        quantity -= 1;
    }
    else{
        quantity=0
    }
    itemQuantity.innerHTML = quantity;
}

function increaseQuantity(){
    let itemQuantity = this.parentNode.querySelector(".qunty");
    let quantity = parseInt(itemQuantity.innerHTML);
    quantity += 1;
    itemQuantity.innerHTML = quantity;
}

var selectedItems=[]


document.querySelectorAll(".add-btn").forEach((button)=>{
    button.addEventListener("click",function(){
        var itemCost=this.parentNode.querySelector(".itemPrice");
        var quantity=this.parentNode.querySelector(".qunty");
        var totalCost=parseInt(itemCost.innerHTML.slice(1), 10)*parseInt(quantity.innerHTML)
        var delIcon=this.parentNode.querySelector(".deleteIcon")
        var priceDisplay=document.getElementById("priceDisplay")

        this.style.backgroundColor="#FE9AA4"
        delIcon.style.display="flex"

        var price=parseInt(priceDisplay.innerHTML.slice(1),10)
        price=price+parseInt(totalCost)

        priceDisplay.innerHTML="$"+price
        
        var selectedItem={
            selectedItemName:this.parentNode.querySelector(".itemName").innerHTML,
            selectedItemQnty:this.parentNode.querySelector(".qunty").innerHTML,
            selectedItemPrice:parseInt(this.parentNode.querySelector(".itemPrice").innerHTML.slice(1),10),
            totalCost:totalCost
        }
        selectedItems.push(selectedItem)
        
    // confirmOrder(selectedItems)
    })
});
document.querySelectorAll(".deleteButton").forEach((button)=>{
    button.addEventListener("click",function(){
        var itemCost=this.parentNode.querySelector(".itemPrice");
        var quantity=this.parentNode.querySelector(".qunty");
        var totalCost=parseInt(itemCost.innerHTML.slice(1), 10)*parseInt(quantity.innerHTML)
        var delIcon=this.parentNode.querySelector(".deleteIcon")
        var priceDisplay=document.getElementById("priceDisplay")
        var addBtn=this.parentNode.querySelector(".add-btn");
        var price=parseInt(priceDisplay.innerHTML.slice(1),10)
        console.log(price)
        price=price-parseInt(totalCost)
        priceDisplay.innerHTML="$"+price

        delIcon.style.display="none"
        addBtn.style.backgroundColor="rgb(251, 94, 94)"

        quantity.innerHTML="1"
    })
})

// document.getElementById("confirmOrderBtn").addEventListener("click",confirmOrder)


  
  
  
  
  
  