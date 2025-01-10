//contains objects that describe the products
//each component of the products
const products = [
  { name: "Produto 1", image: "static/img/box.png" },
  { name: "Produto 2", image: "static/img/box.png" },
  { name: "Produto 3", image: "static/img/box.png" },
  { name: "Produto 4", image: "static/img/box.png" },
  { name: "Produto 5", image: "static/img/box.png" },
  { name: "Produto 6", image: "static/img/box.png" },
  { name: "Produto 7", image: "static/img/box.png" },
  { name: "Produto 8", image: "static/img/box.png" },
  { name: "Produto 9", image: "static/img/box.png" },
];

//creates the structure of the product element
function createProductElement(product) {

  //creates the div element for each product
  const productItem = document.createElement("div");
  productItem.classList.add("product-item");

  //creates the img element for each product
  const productImage = document.createElement("img");
  productImage.src = product.image;
  productImage.alt = product.name;

  //creates the span/name element for each product
  const productName = document.createElement("span");
  productName.textContent = product.name;

  productItem.appendChild(productImage);
  productItem.appendChild(productName);

  return productItem;
}

//create an html element for each product
function displayProducts() {
  const productList = document.getElementById("productList");
  productList.innerHTML = "";

  products.forEach(product => {
      const productItem = createProductElement(product);
      productList.appendChild(productItem);
  });
}

//filters the product whose name is entered
function filterProducts() {

  const searchInput = document.getElementById("searchInput");
  const filter = searchInput.value.toLowerCase();
  const filteredProducts = products.filter(product => product.name.toLowerCase().includes(filter));

  const productList = document.getElementById("productList");
  productList.innerHTML = "";

  filteredProducts.forEach(product => {
      const productItem = createProductElement(product);
      productList.appendChild(productItem);
  });
}


//displays all products
window.onload = function () {
  displayProducts();
};


