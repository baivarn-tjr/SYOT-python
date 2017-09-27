"use strict";

var QuantityBox = React.createClass({
  displayName: "QuantityBox",

  getInitialState: function getInitialState() {
    return { value: 1 };
  },
  onDecrement: function onDecrement(e) {
    if (this.state.value <= 0) return;
    this.setState({ value: --this.state.value });
  },
  onIncrement: function onIncrement(e) {
    this.setState({ value: ++this.state.value });
  },
  render: function render() {
    return React.createElement(
      "div",
      { className: "qty-box" },
      React.createElement(
        "span",
        { className: "dec", onClick: this.onDecrement, onTouchStart: this.onDecrement },
        "–"
      ),
      React.createElement(
        "span",
        { className: "qty" },
        this.state.value
      ),
      React.createElement(
        "span",
        { className: "inc", onClick: this.onIncrement, onTouchStart: this.onIncrement },
        "+"
      )
    );
  }
});

React.render(React.createElement(QuantityBox, null), document.body);