function likes() {
    var likes = document.querySelector(".likeAmigo");
    console.log(likes);
    var likesNumber = parseInt(likes.innerHTML);
    likesNumber++;
    likes.innerHTML = likesNumber + " Like(s)";
}