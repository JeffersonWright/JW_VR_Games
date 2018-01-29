(function() {

    var gameSections = document.getElementsByClassName('gamename');
    for(var i = 0; i < gameSections.length; i++) {
        gameSections[i].addEventListener('mouseover', function Hover() {
            var children = this.children;
            for(var i = 0; i < children.length; i++) {
                var child = children[i];
                if (child.className === 'hidden') {
                    child.className = 'unhidden';
                }
            }
        }
);
        gameSections[i].addEventListener('mouseout', function EndHover() {
            var children = this.children;
            for(var i = 0; i < children.length; i++) {
                var child = children[i];
                if (child.className === 'unhidden') {
                    child.className = 'hidden';
                    document.getElementById("thumb").src ="";
                }
            }
        });
    }

}());
