$(() => {
    let addPostForm = $(".add-post")
    addPostForm.hide();

    $("#add-post-button").click(() => {
        addPostForm.show();
        $("#add-post-button").hide();
    });
    $("#cancel-post").click(() => {
        addPostForm.hide();
        $("#add-post-button").show();
    });
});