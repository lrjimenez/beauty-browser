$(document).ready(()=>{
    $(".product-type-radio").on("click", (evt)=>{
        const args = {productTypeId:evt.target.value};
        console.log(args);
        $.get("/api/brand-list", args, response => {
            console.log(response);
            let options = "";
            for (const brand of response) {
                options = options + (`<option> ${brand} </option>`)
            }
            $("#brand-menu").html(options)
        })
    });
});