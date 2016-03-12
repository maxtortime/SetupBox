/**
 * Created by tkim on 2016. 3. 11..
 */
$(function() {
    $.contextMenu({
        selector: '.files',
        callback: function(key) {
            if (key == "rename") {
                var name = prompt("Please input new file name");

                $.post('/' + key, {
                    old_name: $(this.context).text(),
                    new_name: name,
                    directory_root: $("#folder_path").val(),
                    path: $(this.context).attr('id')
                });
            }
            else {
                $.post('/'+key, {
                    path: $(this.context).attr('id'),
                    directory_root:$("#folder_path").val()
                });
            }

            location.reload();
        },
        items: {
            "rename": {name: "이름 바꾸기", icon: "edit"},
            "delete": {name: "삭제하기", icon: "delete"}
        }
    });
});

$(function() {
    $.contextMenu({
        selector: '.folders',
        callback: function(key) {
            if (key == "rename") {
                var name = prompt("Please input new file name");

                $.post('/' + key, {
                    old_name: $(this.context).text(),
                    new_name: name,
                    directory_root: $("#folder_path").val(),
                    path: $(this.context).attr('id')
                });
            }
            else if (key == "move") {
                var new_path = prompt("Please input new path");

                $.post('/' + key, {
                    old_path: $(this.context).attr('id'),
                    directory_root: $("#folder_path").val(),
                    new_path : new_path
                });
            }
            else {
                $.post('/'+key,{ path:$(this.context).attr('id'),
                    directory_root:$("#folder_path").val() });
            }

            location.reload();

        },
        items: {
            "rename": {name: "이름 바꾸기", icon: "edit"},
            "delete": {name: "삭제하기", icon: "delete"}
        }
    });
});
