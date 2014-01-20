Summary:	X11/GL screen capture tool
Summary(pl.UTF-8):	Narzędzie do wykonywania zrzutów ekranu X11/GL
Name:		captury
Version:	0.3.0
Release:	2
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.debian.org/debian/pool/main/c/captury/%{name}_%{version}~svn158.orig.tar.gz
# Source0-md5:	54b2de085bd83cb11da6598f6fa46198
Patch0:		%{name}-libpng.patch
URL:		http://rm-rf.in/captury
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	elfutils-devel
BuildRequires:	libcaptury-devel
BuildRequires:	libpng-devel >= 1.2
BuildRequires:	pkgconfig >= 1:0.17.2
BuildRequires:	xorg-lib-libX11-devel
Requires:	/usr/%{_lib}/libGL.so.1
Requires:	/usr/%{_lib}/libX11.so.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Captury is a screen capture application, primarly done for recording
OpenGL games.

%description -l pl.UTF-8
Captury to aplikacja do wykonywania zrzutów ekranów, przeznaczona
głównie do nagrywania gier OpenGL

%prep
%setup -q -n %{name}-%{version}~svn158.orig
%patch0 -p1

%build
%configure
# override NATIVE_ paths to symlink sonames and avoid depending on -devel packages
%{__make} \
	NATIVE_LIBGL=/usr/%{_lib}/libGL.so.1 \
	NATIVE_LIBX11=/usr/%{_lib}/libX11.so.6

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	NATIVE_LIBGL=/usr/%{_lib}/libGL.so.1 \
	NATIVE_LIBX11=/usr/%{_lib}/libX11.so.6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/captury.conf
%attr(755,root,root) %{_bindir}/captury
%dir %{_libdir}/captury
%attr(755,root,root) %{_libdir}/captury/libGLcaptury.so
# symlinks to libGLcaptury
%attr(755,root,root) %{_libdir}/captury/libGL.so.1
%attr(755,root,root) %{_libdir}/captury/libGL.so
%attr(755,root,root) %{_libdir}/captury/libX11.so.6
%attr(755,root,root) %{_libdir}/captury/libX11.so
# symlinks to system libGL and libX11
%attr(755,root,root) %{_libdir}/captury/libGLnative.so
%attr(755,root,root) %{_libdir}/captury/libX11native.so
