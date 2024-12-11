const menu_toggle = $('.menu-toggle');
const sidebar = $('.sidebar');

menu_toggle.on('click', function() {
    menu_toggle.toggleClass('is-active');
    sidebar.toggleClass('is-active');
});