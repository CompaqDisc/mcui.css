function initTooltip() {
    const tooltips = Array.from(document.querySelectorAll('[data-tooltip]'));

    tooltips.map(tooltip => {
        tooltip.addEventListener('mouseover', function() {
            let tooltip_span = document.getElementById('tooltip');
            tooltip_span.childNodes[1].innerText = this.getAttribute('data-tooltip');
            tooltip_span.childNodes[3].innerText = this.getAttribute('data-tooltip-description');
            tooltip_span.hidden = false;

            this.addEventListener('mousemove', function(event) {
                tooltip_span.style.top = event.clientY - 45 + 'px';
                tooltip_span.style.left = event.clientX + 20 + 'px';
            });

            this.addEventListener('mouseleave', function(event) {
                tooltip_span.hidden = true;
            })
        });
	})
}

initTooltip();