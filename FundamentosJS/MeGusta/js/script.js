function likes() {
    var likes = document.querySelector(".btnLikes-button");
    console.log(likes);
    var likesNumber = parseInt(likes.innerHTML);
    likesNumber++;
    likes.innerHTML = likesNumber + " Like(s)";
}