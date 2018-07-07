let sponsors_html = document.querySelector('.patreons');

sponsors_json.spons.forEach((category, i) => {
    category.sponsors.forEach((sponsor, i) => {
        sponsors_html.innerHTML += ` 
            <div class='sponsor'>
                <img src='${sponsor.image1}'>
                <div class='details'>
                    <h2>${sponsor.sponsName}</h2>
                    <p class='body'>${sponsor.body}</p>
                    <p class='contact_no'>${sponsor.contact}</p>
                    <p class='website'><a href='${sponsor.website_url}'>website</a></p>
                </div>
            </div>`;
    })
});

console.log(sponsors_html);
console.log(sponsors_json.spons);