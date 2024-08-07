#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v13
# autospec commit: dc0ff31
#
%define keepstatic 1
Name     : tk
Version  : 8.6.14
Release  : 34
URL      : https://sourceforge.net/projects/tcl/files/Tcl/8.6.14/tk8.6.14-src.tar.gz
Source0  : https://sourceforge.net/projects/tcl/files/Tcl/8.6.14/tk8.6.14-src.tar.gz
Summary  : Tk graphical toolkit for the Tcl scripting language.
Group    : Development/Tools
License  : TCL
Requires: tk-bin = %{version}-%{release}
Requires: tk-license = %{version}-%{release}
Requires: tk-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : libXScrnSaver-dev
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xft)
BuildRequires : tcl
BuildRequires : tcl-dev
BuildRequires : tcl-staticdev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The Tcl (Tool Command Language) provides a powerful platform for
creating integration applications that tie together diverse
applications, protocols, devices, and frameworks.  When paired with
the Tk toolkit, Tcl provides the fastest and most powerful way to
create GUI applications that run on PCs, Unix, and Mac OS X.  Tcl
can also be used for a variety of web-related tasks and for creating
powerful command languages for applications.

%package bin
Summary: bin components for the tk package.
Group: Binaries
Requires: tk-license = %{version}-%{release}

%description bin
bin components for the tk package.


%package dev
Summary: dev components for the tk package.
Group: Development
Requires: tk-bin = %{version}-%{release}
Provides: tk-devel = %{version}-%{release}
Requires: tk = %{version}-%{release}
Requires: tcl-dev
Requires: tk-staticdev = %{version}-%{release}

%description dev
dev components for the tk package.


%package extras
Summary: extras components for the tk package.
Group: Default

%description extras
extras components for the tk package.


%package license
Summary: license components for the tk package.
Group: Default

%description license
license components for the tk package.


%package man
Summary: man components for the tk package.
Group: Default

%description man
man components for the tk package.


%package staticdev
Summary: staticdev components for the tk package.
Group: Default
Requires: tk-dev = %{version}-%{release}

%description staticdev
staticdev components for the tk package.


%prep
%setup -q -n tk8.6.14
cd %{_builddir}/tk8.6.14
pushd ..
cp -a tk8.6.14 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1720021067
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
pushd unix/
export GOAMD64=v2
%configure
make  %{?_smp_mflags}
popd

unset PKG_CONFIG_PATH
pushd ../buildavx2/unix/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure
make  %{?_smp_mflags}
popd
%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1720021067
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tk
cp %{_builddir}/tk%{version}/compat/license.terms %{buildroot}/usr/share/package-licenses/tk/58769f631eb2c8ded0c274ab1d399085cc7aa845 || :
cp %{_builddir}/tk%{version}/doc/license.terms %{buildroot}/usr/share/package-licenses/tk/58769f631eb2c8ded0c274ab1d399085cc7aa845 || :
cp %{_builddir}/tk%{version}/library/demos/license.terms %{buildroot}/usr/share/package-licenses/tk/58769f631eb2c8ded0c274ab1d399085cc7aa845 || :
cp %{_builddir}/tk%{version}/library/license.terms %{buildroot}/usr/share/package-licenses/tk/58769f631eb2c8ded0c274ab1d399085cc7aa845 || :
cp %{_builddir}/tk%{version}/license.terms %{buildroot}/usr/share/package-licenses/tk/58769f631eb2c8ded0c274ab1d399085cc7aa845 || :
cp %{_builddir}/tk%{version}/macosx/license.terms %{buildroot}/usr/share/package-licenses/tk/58769f631eb2c8ded0c274ab1d399085cc7aa845 || :
cp %{_builddir}/tk%{version}/tests/license.terms %{buildroot}/usr/share/package-licenses/tk/58769f631eb2c8ded0c274ab1d399085cc7aa845 || :
cp %{_builddir}/tk%{version}/unix/license.terms %{buildroot}/usr/share/package-licenses/tk/58769f631eb2c8ded0c274ab1d399085cc7aa845 || :
cp %{_builddir}/tk%{version}/win/license.terms %{buildroot}/usr/share/package-licenses/tk/58769f631eb2c8ded0c274ab1d399085cc7aa845 || :
cp %{_builddir}/tk%{version}/xlib/X11/license.terms %{buildroot}/usr/share/package-licenses/tk/58769f631eb2c8ded0c274ab1d399085cc7aa845 || :
cp %{_builddir}/tk%{version}/xlib/license.terms %{buildroot}/usr/share/package-licenses/tk/58769f631eb2c8ded0c274ab1d399085cc7aa845 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/unix/
%make_install_v3 install-private-headers
popd
pushd unix/
GOAMD64=v2
%make_install install-private-headers
popd
## install_append content
ln -s wish8.6 %{buildroot}/usr/bin/wish
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib/tk8.6/bgerror.tcl
/usr/lib/tk8.6/button.tcl
/usr/lib/tk8.6/choosedir.tcl
/usr/lib/tk8.6/clrpick.tcl
/usr/lib/tk8.6/comdlg.tcl
/usr/lib/tk8.6/console.tcl
/usr/lib/tk8.6/demos/README
/usr/lib/tk8.6/demos/anilabel.tcl
/usr/lib/tk8.6/demos/aniwave.tcl
/usr/lib/tk8.6/demos/arrow.tcl
/usr/lib/tk8.6/demos/bind.tcl
/usr/lib/tk8.6/demos/bitmap.tcl
/usr/lib/tk8.6/demos/browse
/usr/lib/tk8.6/demos/button.tcl
/usr/lib/tk8.6/demos/check.tcl
/usr/lib/tk8.6/demos/clrpick.tcl
/usr/lib/tk8.6/demos/colors.tcl
/usr/lib/tk8.6/demos/combo.tcl
/usr/lib/tk8.6/demos/cscroll.tcl
/usr/lib/tk8.6/demos/ctext.tcl
/usr/lib/tk8.6/demos/dialog1.tcl
/usr/lib/tk8.6/demos/dialog2.tcl
/usr/lib/tk8.6/demos/en.msg
/usr/lib/tk8.6/demos/entry1.tcl
/usr/lib/tk8.6/demos/entry2.tcl
/usr/lib/tk8.6/demos/entry3.tcl
/usr/lib/tk8.6/demos/filebox.tcl
/usr/lib/tk8.6/demos/floor.tcl
/usr/lib/tk8.6/demos/fontchoose.tcl
/usr/lib/tk8.6/demos/form.tcl
/usr/lib/tk8.6/demos/goldberg.tcl
/usr/lib/tk8.6/demos/hello
/usr/lib/tk8.6/demos/hscale.tcl
/usr/lib/tk8.6/demos/icon.tcl
/usr/lib/tk8.6/demos/image1.tcl
/usr/lib/tk8.6/demos/image2.tcl
/usr/lib/tk8.6/demos/images/earth.gif
/usr/lib/tk8.6/demos/images/earthmenu.png
/usr/lib/tk8.6/demos/images/earthris.gif
/usr/lib/tk8.6/demos/images/flagdown.xbm
/usr/lib/tk8.6/demos/images/flagup.xbm
/usr/lib/tk8.6/demos/images/gray25.xbm
/usr/lib/tk8.6/demos/images/letters.xbm
/usr/lib/tk8.6/demos/images/noletter.xbm
/usr/lib/tk8.6/demos/images/ouster.png
/usr/lib/tk8.6/demos/images/pattern.xbm
/usr/lib/tk8.6/demos/images/tcllogo.gif
/usr/lib/tk8.6/demos/images/teapot.ppm
/usr/lib/tk8.6/demos/items.tcl
/usr/lib/tk8.6/demos/ixset
/usr/lib/tk8.6/demos/knightstour.tcl
/usr/lib/tk8.6/demos/label.tcl
/usr/lib/tk8.6/demos/labelframe.tcl
/usr/lib/tk8.6/demos/license.terms
/usr/lib/tk8.6/demos/mclist.tcl
/usr/lib/tk8.6/demos/menu.tcl
/usr/lib/tk8.6/demos/menubu.tcl
/usr/lib/tk8.6/demos/msgbox.tcl
/usr/lib/tk8.6/demos/nl.msg
/usr/lib/tk8.6/demos/paned1.tcl
/usr/lib/tk8.6/demos/paned2.tcl
/usr/lib/tk8.6/demos/pendulum.tcl
/usr/lib/tk8.6/demos/plot.tcl
/usr/lib/tk8.6/demos/puzzle.tcl
/usr/lib/tk8.6/demos/radio.tcl
/usr/lib/tk8.6/demos/rmt
/usr/lib/tk8.6/demos/rolodex
/usr/lib/tk8.6/demos/ruler.tcl
/usr/lib/tk8.6/demos/sayings.tcl
/usr/lib/tk8.6/demos/search.tcl
/usr/lib/tk8.6/demos/spin.tcl
/usr/lib/tk8.6/demos/states.tcl
/usr/lib/tk8.6/demos/style.tcl
/usr/lib/tk8.6/demos/tclIndex
/usr/lib/tk8.6/demos/tcolor
/usr/lib/tk8.6/demos/text.tcl
/usr/lib/tk8.6/demos/textpeer.tcl
/usr/lib/tk8.6/demos/timer
/usr/lib/tk8.6/demos/toolbar.tcl
/usr/lib/tk8.6/demos/tree.tcl
/usr/lib/tk8.6/demos/ttkbut.tcl
/usr/lib/tk8.6/demos/ttkmenu.tcl
/usr/lib/tk8.6/demos/ttknote.tcl
/usr/lib/tk8.6/demos/ttkpane.tcl
/usr/lib/tk8.6/demos/ttkprogress.tcl
/usr/lib/tk8.6/demos/ttkscale.tcl
/usr/lib/tk8.6/demos/twind.tcl
/usr/lib/tk8.6/demos/unicodeout.tcl
/usr/lib/tk8.6/demos/vscale.tcl
/usr/lib/tk8.6/demos/widget
/usr/lib/tk8.6/dialog.tcl
/usr/lib/tk8.6/entry.tcl
/usr/lib/tk8.6/focus.tcl
/usr/lib/tk8.6/fontchooser.tcl
/usr/lib/tk8.6/iconlist.tcl
/usr/lib/tk8.6/icons.tcl
/usr/lib/tk8.6/images/README
/usr/lib/tk8.6/images/logo.eps
/usr/lib/tk8.6/images/logo100.gif
/usr/lib/tk8.6/images/logo64.gif
/usr/lib/tk8.6/images/logoLarge.gif
/usr/lib/tk8.6/images/logoMed.gif
/usr/lib/tk8.6/images/pwrdLogo.eps
/usr/lib/tk8.6/images/pwrdLogo100.gif
/usr/lib/tk8.6/images/pwrdLogo150.gif
/usr/lib/tk8.6/images/pwrdLogo175.gif
/usr/lib/tk8.6/images/pwrdLogo200.gif
/usr/lib/tk8.6/images/pwrdLogo75.gif
/usr/lib/tk8.6/images/tai-ku.gif
/usr/lib/tk8.6/listbox.tcl
/usr/lib/tk8.6/megawidget.tcl
/usr/lib/tk8.6/menu.tcl
/usr/lib/tk8.6/mkpsenc.tcl
/usr/lib/tk8.6/msgbox.tcl
/usr/lib/tk8.6/msgs/cs.msg
/usr/lib/tk8.6/msgs/da.msg
/usr/lib/tk8.6/msgs/de.msg
/usr/lib/tk8.6/msgs/el.msg
/usr/lib/tk8.6/msgs/en.msg
/usr/lib/tk8.6/msgs/en_gb.msg
/usr/lib/tk8.6/msgs/eo.msg
/usr/lib/tk8.6/msgs/es.msg
/usr/lib/tk8.6/msgs/fi.msg
/usr/lib/tk8.6/msgs/fr.msg
/usr/lib/tk8.6/msgs/hu.msg
/usr/lib/tk8.6/msgs/it.msg
/usr/lib/tk8.6/msgs/nl.msg
/usr/lib/tk8.6/msgs/pl.msg
/usr/lib/tk8.6/msgs/pt.msg
/usr/lib/tk8.6/msgs/ru.msg
/usr/lib/tk8.6/msgs/sv.msg
/usr/lib/tk8.6/msgs/zh_cn.msg
/usr/lib/tk8.6/obsolete.tcl
/usr/lib/tk8.6/optMenu.tcl
/usr/lib/tk8.6/palette.tcl
/usr/lib/tk8.6/panedwindow.tcl
/usr/lib/tk8.6/safetk.tcl
/usr/lib/tk8.6/scale.tcl
/usr/lib/tk8.6/scrlbar.tcl
/usr/lib/tk8.6/spinbox.tcl
/usr/lib/tk8.6/tclIndex
/usr/lib/tk8.6/tearoff.tcl
/usr/lib/tk8.6/text.tcl
/usr/lib/tk8.6/tk.tcl
/usr/lib/tk8.6/tkAppInit.c
/usr/lib/tk8.6/tkfbox.tcl
/usr/lib/tk8.6/ttk/altTheme.tcl
/usr/lib/tk8.6/ttk/aquaTheme.tcl
/usr/lib/tk8.6/ttk/button.tcl
/usr/lib/tk8.6/ttk/clamTheme.tcl
/usr/lib/tk8.6/ttk/classicTheme.tcl
/usr/lib/tk8.6/ttk/combobox.tcl
/usr/lib/tk8.6/ttk/cursors.tcl
/usr/lib/tk8.6/ttk/defaults.tcl
/usr/lib/tk8.6/ttk/entry.tcl
/usr/lib/tk8.6/ttk/fonts.tcl
/usr/lib/tk8.6/ttk/menubutton.tcl
/usr/lib/tk8.6/ttk/notebook.tcl
/usr/lib/tk8.6/ttk/panedwindow.tcl
/usr/lib/tk8.6/ttk/progress.tcl
/usr/lib/tk8.6/ttk/scale.tcl
/usr/lib/tk8.6/ttk/scrollbar.tcl
/usr/lib/tk8.6/ttk/sizegrip.tcl
/usr/lib/tk8.6/ttk/spinbox.tcl
/usr/lib/tk8.6/ttk/treeview.tcl
/usr/lib/tk8.6/ttk/ttk.tcl
/usr/lib/tk8.6/ttk/utils.tcl
/usr/lib/tk8.6/ttk/vistaTheme.tcl
/usr/lib/tk8.6/ttk/winTheme.tcl
/usr/lib/tk8.6/ttk/xpTheme.tcl
/usr/lib/tk8.6/unsupported.tcl
/usr/lib/tk8.6/xmfbox.tcl
/usr/lib64/tk8.6/pkgIndex.tcl
/usr/lib64/tkConfig.sh

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/wish8.6
/usr/bin/wish
/usr/bin/wish8.6

%files dev
%defattr(-,root,root,-)
/usr/include/tk.h
/usr/include/tkDecls.h
/usr/include/tkInt.h
/usr/include/tkIntDecls.h
/usr/include/tkIntPlatDecls.h
/usr/include/tkIntXlibDecls.h
/usr/include/tkPlatDecls.h
/usr/include/tkPort.h
/usr/include/tkUnixDefault.h
/usr/include/tkUnixInt.h
/usr/include/tkUnixPort.h
/usr/include/ttkDecls.h
/usr/include/ttkTheme.h
/usr/lib64/pkgconfig/tk.pc
/usr/share/man/man3/FindPhoto.3
/usr/share/man/man3/FontId.3
/usr/share/man/man3/MeasureChar.3
/usr/share/man/man3/Tk_3DBorderColor.3
/usr/share/man/man3/Tk_3DBorderGC.3
/usr/share/man/man3/Tk_3DHorizontalBevel.3
/usr/share/man/man3/Tk_3DVerticalBevel.3
/usr/share/man/man3/Tk_AddOption.3
/usr/share/man/man3/Tk_Alloc3DBorderFromObj.3
/usr/share/man/man3/Tk_AllocBitmapFromObj.3
/usr/share/man/man3/Tk_AllocColorFromObj.3
/usr/share/man/man3/Tk_AllocCursorFromObj.3
/usr/share/man/man3/Tk_AllocFontFromObj.3
/usr/share/man/man3/Tk_AttachHWND.3
/usr/share/man/man3/Tk_Attributes.3
/usr/share/man/man3/Tk_BindEvent.3
/usr/share/man/man3/Tk_CanvasDrawableCoords.3
/usr/share/man/man3/Tk_CanvasEventuallyRedraw.3
/usr/share/man/man3/Tk_CanvasGetCoord.3
/usr/share/man/man3/Tk_CanvasPsBitmap.3
/usr/share/man/man3/Tk_CanvasPsColor.3
/usr/share/man/man3/Tk_CanvasPsFont.3
/usr/share/man/man3/Tk_CanvasPsPath.3
/usr/share/man/man3/Tk_CanvasPsStipple.3
/usr/share/man/man3/Tk_CanvasPsY.3
/usr/share/man/man3/Tk_CanvasSetStippleOrigin.3
/usr/share/man/man3/Tk_CanvasTagsOption.3
/usr/share/man/man3/Tk_CanvasTextInfo.3
/usr/share/man/man3/Tk_CanvasTkwin.3
/usr/share/man/man3/Tk_CanvasWindowCoords.3
/usr/share/man/man3/Tk_ChangeWindowAttributes.3
/usr/share/man/man3/Tk_Changes.3
/usr/share/man/man3/Tk_CharBbox.3
/usr/share/man/man3/Tk_Class.3
/usr/share/man/man3/Tk_ClearSelection.3
/usr/share/man/man3/Tk_ClipboardAppend.3
/usr/share/man/man3/Tk_ClipboardClear.3
/usr/share/man/man3/Tk_CollapseMotionEvents.3
/usr/share/man/man3/Tk_Colormap.3
/usr/share/man/man3/Tk_ComputeTextLayout.3
/usr/share/man/man3/Tk_ConfigureInfo.3
/usr/share/man/man3/Tk_ConfigureValue.3
/usr/share/man/man3/Tk_ConfigureWidget.3
/usr/share/man/man3/Tk_ConfigureWindow.3
/usr/share/man/man3/Tk_CoordsToWindow.3
/usr/share/man/man3/Tk_CreateBinding.3
/usr/share/man/man3/Tk_CreateBindingTable.3
/usr/share/man/man3/Tk_CreateClientMessageHandler.3
/usr/share/man/man3/Tk_CreateErrorHandler.3
/usr/share/man/man3/Tk_CreateEventHandler.3
/usr/share/man/man3/Tk_CreateGenericHandler.3
/usr/share/man/man3/Tk_CreateImageType.3
/usr/share/man/man3/Tk_CreateItemType.3
/usr/share/man/man3/Tk_CreateOptionTable.3
/usr/share/man/man3/Tk_CreatePhotoImageFormat.3
/usr/share/man/man3/Tk_CreateSelHandler.3
/usr/share/man/man3/Tk_CreateWindow.3
/usr/share/man/man3/Tk_CreateWindowFromPath.3
/usr/share/man/man3/Tk_DefineBitmap.3
/usr/share/man/man3/Tk_DefineCursor.3
/usr/share/man/man3/Tk_DeleteAllBindings.3
/usr/share/man/man3/Tk_DeleteBinding.3
/usr/share/man/man3/Tk_DeleteBindingTable.3
/usr/share/man/man3/Tk_DeleteClientMessageHandler.3
/usr/share/man/man3/Tk_DeleteErrorHandler.3
/usr/share/man/man3/Tk_DeleteEventHandler.3
/usr/share/man/man3/Tk_DeleteGenericHandler.3
/usr/share/man/man3/Tk_DeleteImage.3
/usr/share/man/man3/Tk_DeleteOptionTable.3
/usr/share/man/man3/Tk_DeleteSelHandler.3
/usr/share/man/man3/Tk_Depth.3
/usr/share/man/man3/Tk_DestroyWindow.3
/usr/share/man/man3/Tk_Display.3
/usr/share/man/man3/Tk_DisplayName.3
/usr/share/man/man3/Tk_DistanceToTextLayout.3
/usr/share/man/man3/Tk_Draw3DPolygon.3
/usr/share/man/man3/Tk_Draw3DRectangle.3
/usr/share/man/man3/Tk_DrawChars.3
/usr/share/man/man3/Tk_DrawFocusHighlight.3
/usr/share/man/man3/Tk_DrawTextLayout.3
/usr/share/man/man3/Tk_Fill3DPolygon.3
/usr/share/man/man3/Tk_Fill3DRectangle.3
/usr/share/man/man3/Tk_FindPhoto.3
/usr/share/man/man3/Tk_FontId.3
/usr/share/man/man3/Tk_Free3DBorder.3
/usr/share/man/man3/Tk_Free3DBorderFromObj.3
/usr/share/man/man3/Tk_FreeBitmap.3
/usr/share/man/man3/Tk_FreeBitmapFromObj.3
/usr/share/man/man3/Tk_FreeColor.3
/usr/share/man/man3/Tk_FreeColorFromObj.3
/usr/share/man/man3/Tk_FreeColormap.3
/usr/share/man/man3/Tk_FreeConfigOptions.3
/usr/share/man/man3/Tk_FreeCursor.3
/usr/share/man/man3/Tk_FreeCursorFromObj.3
/usr/share/man/man3/Tk_FreeFont.3
/usr/share/man/man3/Tk_FreeFontFromObj.3
/usr/share/man/man3/Tk_FreeGC.3
/usr/share/man/man3/Tk_FreeImage.3
/usr/share/man/man3/Tk_FreeOptions.3
/usr/share/man/man3/Tk_FreePixmap.3
/usr/share/man/man3/Tk_FreeSavedOptions.3
/usr/share/man/man3/Tk_FreeTextLayout.3
/usr/share/man/man3/Tk_FreeXId.3
/usr/share/man/man3/Tk_GeometryRequest.3
/usr/share/man/man3/Tk_Get3DBorder.3
/usr/share/man/man3/Tk_Get3DBorderFromObj.3
/usr/share/man/man3/Tk_GetAllBindings.3
/usr/share/man/man3/Tk_GetAnchor.3
/usr/share/man/man3/Tk_GetAnchorFromObj.3
/usr/share/man/man3/Tk_GetAtomName.3
/usr/share/man/man3/Tk_GetBinding.3
/usr/share/man/man3/Tk_GetBitmap.3
/usr/share/man/man3/Tk_GetBitmapFromObj.3
/usr/share/man/man3/Tk_GetCapStyle.3
/usr/share/man/man3/Tk_GetColor.3
/usr/share/man/man3/Tk_GetColorByValue.3
/usr/share/man/man3/Tk_GetColorFromObj.3
/usr/share/man/man3/Tk_GetColormap.3
/usr/share/man/man3/Tk_GetCursor.3
/usr/share/man/man3/Tk_GetCursorFromData.3
/usr/share/man/man3/Tk_GetCursorFromObj.3
/usr/share/man/man3/Tk_GetDash.3
/usr/share/man/man3/Tk_GetFont.3
/usr/share/man/man3/Tk_GetFontFromObj.3
/usr/share/man/man3/Tk_GetFontMetrics.3
/usr/share/man/man3/Tk_GetGC.3
/usr/share/man/man3/Tk_GetHINSTANCE.3
/usr/share/man/man3/Tk_GetHWND.3
/usr/share/man/man3/Tk_GetImage.3
/usr/share/man/man3/Tk_GetImageMasterData.3
/usr/share/man/man3/Tk_GetImageModelData.3
/usr/share/man/man3/Tk_GetItemTypes.3
/usr/share/man/man3/Tk_GetJoinStyle.3
/usr/share/man/man3/Tk_GetJustify.3
/usr/share/man/man3/Tk_GetJustifyFromObj.3
/usr/share/man/man3/Tk_GetMMFromObj.3
/usr/share/man/man3/Tk_GetNumMainWindows.3
/usr/share/man/man3/Tk_GetOption.3
/usr/share/man/man3/Tk_GetOptionInfo.3
/usr/share/man/man3/Tk_GetOptionValue.3
/usr/share/man/man3/Tk_GetPixels.3
/usr/share/man/man3/Tk_GetPixelsFromObj.3
/usr/share/man/man3/Tk_GetPixmap.3
/usr/share/man/man3/Tk_GetRelief.3
/usr/share/man/man3/Tk_GetReliefFromObj.3
/usr/share/man/man3/Tk_GetRootCoords.3
/usr/share/man/man3/Tk_GetScreenMM.3
/usr/share/man/man3/Tk_GetScrollInfo.3
/usr/share/man/man3/Tk_GetScrollInfoObj.3
/usr/share/man/man3/Tk_GetSelection.3
/usr/share/man/man3/Tk_GetUid.3
/usr/share/man/man3/Tk_GetUserInactiveTime.3
/usr/share/man/man3/Tk_GetVRootGeometry.3
/usr/share/man/man3/Tk_GetVisual.3
/usr/share/man/man3/Tk_Grab.3
/usr/share/man/man3/Tk_HWNDToWindow.3
/usr/share/man/man3/Tk_HandleEvent.3
/usr/share/man/man3/Tk_Height.3
/usr/share/man/man3/Tk_IdToWindow.3
/usr/share/man/man3/Tk_ImageChanged.3
/usr/share/man/man3/Tk_Init.3
/usr/share/man/man3/Tk_InitConsoleChannels.3
/usr/share/man/man3/Tk_InitImageArgs.3
/usr/share/man/man3/Tk_InitOptions.3
/usr/share/man/man3/Tk_InitStubs.3
/usr/share/man/man3/Tk_InternAtom.3
/usr/share/man/man3/Tk_InternalBorderBottom.3
/usr/share/man/man3/Tk_InternalBorderLeft.3
/usr/share/man/man3/Tk_InternalBorderRight.3
/usr/share/man/man3/Tk_InternalBorderTop.3
/usr/share/man/man3/Tk_Interp.3
/usr/share/man/man3/Tk_IntersectTextLayout.3
/usr/share/man/man3/Tk_IsContainer.3
/usr/share/man/man3/Tk_IsEmbedded.3
/usr/share/man/man3/Tk_IsMapped.3
/usr/share/man/man3/Tk_IsTopLevel.3
/usr/share/man/man3/Tk_Main.3
/usr/share/man/man3/Tk_MainLoop.3
/usr/share/man/man3/Tk_MainWindow.3
/usr/share/man/man3/Tk_MaintainGeometry.3
/usr/share/man/man3/Tk_MakeWindowExist.3
/usr/share/man/man3/Tk_ManageGeometry.3
/usr/share/man/man3/Tk_MapWindow.3
/usr/share/man/man3/Tk_MeasureChars.3
/usr/share/man/man3/Tk_MinReqHeight.3
/usr/share/man/man3/Tk_MinReqWidth.3
/usr/share/man/man3/Tk_MoveResizeWindow.3
/usr/share/man/man3/Tk_MoveToplevelWindow.3
/usr/share/man/man3/Tk_MoveWindow.3
/usr/share/man/man3/Tk_Name.3
/usr/share/man/man3/Tk_NameOf3DBorder.3
/usr/share/man/man3/Tk_NameOfAnchor.3
/usr/share/man/man3/Tk_NameOfBitmap.3
/usr/share/man/man3/Tk_NameOfCapStyle.3
/usr/share/man/man3/Tk_NameOfColor.3
/usr/share/man/man3/Tk_NameOfCursor.3
/usr/share/man/man3/Tk_NameOfFont.3
/usr/share/man/man3/Tk_NameOfImage.3
/usr/share/man/man3/Tk_NameOfJoinStyle.3
/usr/share/man/man3/Tk_NameOfJustify.3
/usr/share/man/man3/Tk_NameOfRelief.3
/usr/share/man/man3/Tk_NameToWindow.3
/usr/share/man/man3/Tk_Offset.3
/usr/share/man/man3/Tk_OwnSelection.3
/usr/share/man/man3/Tk_Parent.3
/usr/share/man/man3/Tk_ParseArgv.3
/usr/share/man/man3/Tk_PathName.3
/usr/share/man/man3/Tk_PhotoBlank.3
/usr/share/man/man3/Tk_PhotoExpand.3
/usr/share/man/man3/Tk_PhotoGetImage.3
/usr/share/man/man3/Tk_PhotoGetSize.3
/usr/share/man/man3/Tk_PhotoPutBlock.3
/usr/share/man/man3/Tk_PhotoPutZoomedBlock.3
/usr/share/man/man3/Tk_PhotoSetSize.3
/usr/share/man/man3/Tk_PointToChar.3
/usr/share/man/man3/Tk_PostscriptFontName.3
/usr/share/man/man3/Tk_PreserveColormap.3
/usr/share/man/man3/Tk_QueueWindowEvent.3
/usr/share/man/man3/Tk_RedrawImage.3
/usr/share/man/man3/Tk_ReqHeight.3
/usr/share/man/man3/Tk_ReqWidth.3
/usr/share/man/man3/Tk_ResetUserInactiveTime.3
/usr/share/man/man3/Tk_ResizeWindow.3
/usr/share/man/man3/Tk_RestackWindow.3
/usr/share/man/man3/Tk_RestoreSavedOptions.3
/usr/share/man/man3/Tk_RestrictEvents.3
/usr/share/man/man3/Tk_SafeInit.3
/usr/share/man/man3/Tk_Screen.3
/usr/share/man/man3/Tk_ScreenNumber.3
/usr/share/man/man3/Tk_SetAppName.3
/usr/share/man/man3/Tk_SetBackgroundFromBorder.3
/usr/share/man/man3/Tk_SetCaretPos.3
/usr/share/man/man3/Tk_SetClass.3
/usr/share/man/man3/Tk_SetClassProcs.3
/usr/share/man/man3/Tk_SetGrid.3
/usr/share/man/man3/Tk_SetInternalBorder.3
/usr/share/man/man3/Tk_SetInternalBorderEx.3
/usr/share/man/man3/Tk_SetMinimumRequestSize.3
/usr/share/man/man3/Tk_SetOptions.3
/usr/share/man/man3/Tk_SetWindowBackground.3
/usr/share/man/man3/Tk_SetWindowBackgroundPixmap.3
/usr/share/man/man3/Tk_SetWindowBorder.3
/usr/share/man/man3/Tk_SetWindowBorderPixmap.3
/usr/share/man/man3/Tk_SetWindowBorderWidth.3
/usr/share/man/man3/Tk_SetWindowColormap.3
/usr/share/man/man3/Tk_SetWindowVisual.3
/usr/share/man/man3/Tk_SizeOfBitmap.3
/usr/share/man/man3/Tk_SizeOfImage.3
/usr/share/man/man3/Tk_StrictMotif.3
/usr/share/man/man3/Tk_TextLayoutToPostscript.3
/usr/share/man/man3/Tk_TextWidth.3
/usr/share/man/man3/Tk_Uid.3
/usr/share/man/man3/Tk_UndefineCursor.3
/usr/share/man/man3/Tk_UnderlineChars.3
/usr/share/man/man3/Tk_UnderlineTextLayout.3
/usr/share/man/man3/Tk_Ungrab.3
/usr/share/man/man3/Tk_UnmaintainGeometry.3
/usr/share/man/man3/Tk_UnmapWindow.3
/usr/share/man/man3/Tk_UnsetGrid.3
/usr/share/man/man3/Tk_Visual.3
/usr/share/man/man3/Tk_Width.3
/usr/share/man/man3/Tk_WindowId.3
/usr/share/man/man3/Tk_X.3
/usr/share/man/man3/Tk_Y.3
/usr/share/man/man3/Ttk_AddPadding.3
/usr/share/man/man3/Ttk_BoxContains.3
/usr/share/man/man3/Ttk_CreateTheme.3
/usr/share/man/man3/Ttk_ExpandBox.3
/usr/share/man/man3/Ttk_GetBorderFromObj.3
/usr/share/man/man3/Ttk_GetCurrentTheme.3
/usr/share/man/man3/Ttk_GetDefaultTheme.3
/usr/share/man/man3/Ttk_GetPaddingFromObj.3
/usr/share/man/man3/Ttk_GetStickyFromObj.3
/usr/share/man/man3/Ttk_GetTheme.3
/usr/share/man/man3/Ttk_MakeBox.3
/usr/share/man/man3/Ttk_MakePadding.3
/usr/share/man/man3/Ttk_PackBox.3
/usr/share/man/man3/Ttk_PadBox.3
/usr/share/man/man3/Ttk_PlaceBox.3
/usr/share/man/man3/Ttk_RelievePadding.3
/usr/share/man/man3/Ttk_StickBox.3
/usr/share/man/man3/Ttk_UniformPadding.3

%files extras
%defattr(-,root,root,-)
/V3/usr/lib64/libtk8.6.so
/usr/lib64/libtk8.6.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tk/58769f631eb2c8ded0c274ab1d399085cc7aa845

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/wish.1
/usr/share/man/mann/bell.n
/usr/share/man/mann/bind.n
/usr/share/man/mann/bindtags.n
/usr/share/man/mann/bitmap.n
/usr/share/man/mann/busy.n
/usr/share/man/mann/button.n
/usr/share/man/mann/canvas.n
/usr/share/man/mann/checkbutton.n
/usr/share/man/mann/clipboard.n
/usr/share/man/mann/colors.n
/usr/share/man/mann/console.n
/usr/share/man/mann/cursors.n
/usr/share/man/mann/destroy.n
/usr/share/man/mann/entry.n
/usr/share/man/mann/event.n
/usr/share/man/mann/focus.n
/usr/share/man/mann/font.n
/usr/share/man/mann/fontchooser.n
/usr/share/man/mann/frame.n
/usr/share/man/mann/geometry.n
/usr/share/man/mann/grab.n
/usr/share/man/mann/grid.n
/usr/share/man/mann/image.n
/usr/share/man/mann/keysyms.n
/usr/share/man/mann/label.n
/usr/share/man/mann/labelframe.n
/usr/share/man/mann/listbox.n
/usr/share/man/mann/lower.n
/usr/share/man/mann/menu.n
/usr/share/man/mann/menubutton.n
/usr/share/man/mann/message.n
/usr/share/man/mann/option.n
/usr/share/man/mann/options.n
/usr/share/man/mann/pack.n
/usr/share/man/mann/pack_old.n
/usr/share/man/mann/panedwindow.n
/usr/share/man/mann/photo.n
/usr/share/man/mann/place.n
/usr/share/man/mann/radiobutton.n
/usr/share/man/mann/raise.n
/usr/share/man/mann/safe_loadTk.n
/usr/share/man/mann/scale.n
/usr/share/man/mann/scrollbar.n
/usr/share/man/mann/selection.n
/usr/share/man/mann/send.n
/usr/share/man/mann/spinbox.n
/usr/share/man/mann/text.n
/usr/share/man/mann/tk.n
/usr/share/man/mann/tk_bindForTraversal.n
/usr/share/man/mann/tk_bisque.n
/usr/share/man/mann/tk_chooseColor.n
/usr/share/man/mann/tk_chooseDirectory.n
/usr/share/man/mann/tk_dialog.n
/usr/share/man/mann/tk_focusFollowsMouse.n
/usr/share/man/mann/tk_focusNext.n
/usr/share/man/mann/tk_focusPrev.n
/usr/share/man/mann/tk_getOpenFile.n
/usr/share/man/mann/tk_getSaveFile.n
/usr/share/man/mann/tk_library.n
/usr/share/man/mann/tk_mac.n
/usr/share/man/mann/tk_menuBar.n
/usr/share/man/mann/tk_menuSetFocus.n
/usr/share/man/mann/tk_messageBox.n
/usr/share/man/mann/tk_optionMenu.n
/usr/share/man/mann/tk_patchLevel.n
/usr/share/man/mann/tk_popup.n
/usr/share/man/mann/tk_setPalette.n
/usr/share/man/mann/tk_strictMotif.n
/usr/share/man/mann/tk_textCopy.n
/usr/share/man/mann/tk_textCut.n
/usr/share/man/mann/tk_textPaste.n
/usr/share/man/mann/tk_version.n
/usr/share/man/mann/tkerror.n
/usr/share/man/mann/tkwait.n
/usr/share/man/mann/toplevel.n
/usr/share/man/mann/ttk_button.n
/usr/share/man/mann/ttk_checkbutton.n
/usr/share/man/mann/ttk_combobox.n
/usr/share/man/mann/ttk_entry.n
/usr/share/man/mann/ttk_frame.n
/usr/share/man/mann/ttk_image.n
/usr/share/man/mann/ttk_intro.n
/usr/share/man/mann/ttk_label.n
/usr/share/man/mann/ttk_labelframe.n
/usr/share/man/mann/ttk_menubutton.n
/usr/share/man/mann/ttk_notebook.n
/usr/share/man/mann/ttk_panedwindow.n
/usr/share/man/mann/ttk_progressbar.n
/usr/share/man/mann/ttk_radiobutton.n
/usr/share/man/mann/ttk_scale.n
/usr/share/man/mann/ttk_scrollbar.n
/usr/share/man/mann/ttk_separator.n
/usr/share/man/mann/ttk_sizegrip.n
/usr/share/man/mann/ttk_spinbox.n
/usr/share/man/mann/ttk_style.n
/usr/share/man/mann/ttk_treeview.n
/usr/share/man/mann/ttk_vsapi.n
/usr/share/man/mann/ttk_widget.n
/usr/share/man/mann/winfo.n
/usr/share/man/mann/wm.n

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libtkstub8.6.a
