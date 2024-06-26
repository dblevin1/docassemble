/*!
 * bootstrap-fileinput v5.1.3
 * http://plugins.krajee.com/file-input
 *
 * Font Awesome 5 icon theme configuration for bootstrap-fileinput. Requires font awesome 5 assets to be loaded.
 *
 * Author: Kartik Visweswaran
 * Copyright: 2014 - 2020, Kartik Visweswaran, Krajee.com
 *
 * Licensed under the BSD-3-Clause
 * https://github.com/kartik-v/bootstrap-fileinput/blob/master/LICENSE.md
 */
(function ($) {
  "use strict";

  $.fn.fileinputThemes.fas = {
    fileActionSettings: {
      removeIcon: '<i class="fa-solid fa-trash-alt"></i>',
      uploadIcon: '<i class="fa-solid fa-upload"></i>',
      uploadRetryIcon: '<i class="fa-solid fa-redo-alt"></i>',
      downloadIcon: '<i class="fa-solid fa-download"></i>',
      zoomIcon: '<i class="fa-solid fa-search-plus"></i>',
      dragIcon: '<i class="fa-solid fa-arrows-alt"></i>',
      indicatorNew: '<i class="fa-solid fa-plus-circle text-warning"></i>',
      indicatorSuccess: '<i class="fa-solid fa-check-circle text-success"></i>',
      indicatorError:
        '<i class="fa-solid fa-exclamation-circle text-danger"></i>',
      indicatorLoading:
        '<i class="fa-solid fa-hourglass text-body-secondary"></i>',
      indicatorPaused: '<i class="fa fa-pause text-info"></i>',
    },
    layoutTemplates: {
      fileIcon: '<i class="fa-solid fa-file kv-caption-icon"></i> ',
    },
    previewZoomButtonIcons: {
      prev: '<i class="fa-solid fa-caret-left fa-lg"></i>',
      next: '<i class="fa-solid fa-caret-right fa-lg"></i>',
      toggleheader: '<i class="fa-solid fa-fw fa-arrows-alt-v"></i>',
      fullscreen: '<i class="fa-solid fa-fw fa-arrows-alt"></i>',
      borderless: '<i class="fa-solid fa-fw fa-external-link-alt"></i>',
      close: '<i class="fa-solid fa-fw fa-xmark"></i>',
    },
    previewFileIcon: '<i class="fa-solid fa-file"></i>',
    browseIcon: '<i class="fa-solid fa-folder-open"></i>',
    removeIcon: '<i class="fa-solid fa-trash-alt"></i>',
    cancelIcon: '<i class="fa-solid fa-ban"></i>',
    pauseIcon: '<i class="fa-solid fa-pause"></i>',
    uploadIcon: '<i class="fa-solid fa-upload"></i>',
    msgValidationErrorIcon: '<i class="fa-solid fa-exclamation-circle"></i> ',
  };
})(window.jQuery);
