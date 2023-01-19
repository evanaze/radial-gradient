function Like() {
    alert("Liked content.")
}

function Dislike() {
    alert("Disliked content.")
}

export function LikeButton() {
    return (
        <button onClick={Like}>
            👍
        </button>
    );
}

export function DislikeButton() {
    return (
        <button onClick={Dislike}>
            👎
        </button>
    );
}
