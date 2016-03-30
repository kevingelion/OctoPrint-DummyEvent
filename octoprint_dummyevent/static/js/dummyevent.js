$(function() {
  function DummyEventViewModel(parameters) {
    var self = this;

    self.settings = parameters[0];

    self.fire_event = function() {
      $.ajax({
        type: "POST",
        url: "/api/plugin/dummyevent",
        data: JSON.stringify({
          command: 'fire_event'
        }),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        complete: function(data) {
          console.log(data);
        },
        error: function(jqXHR, exception) {
          console.log(jqXHR);
        }
      });
    };
  }

  ADDITIONAL_VIEWMODELS.push([
    DummyEventViewModel, ["settingsViewModel"],
    ["#settings_plugin_dummyevent"]
  ]);
});
