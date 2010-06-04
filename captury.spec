Summary:	screen capture tool
Summary(pl.UTF-8):	Narzędzie do wykonywania zrzutów ekranu
Name:		captury
Version:	0.3.0
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.debian.org/debian/pool/main/c/captury/%{name}_%{version}~svn158.orig.tar.gz
# Source0-md5:	54b2de085bd83cb11da6598f6fa46198
URL:		http://rm-rf.in/captury
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	libcaptury-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Captury is a screen capture application, primarly done for recording
OpenGl games.

%package devel
Summary:	Header files and develpment documentation for captury
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumetacja do captury
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and develpment documentation for captury.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do captury.

%package static
Summary:	Static captury library
Summary(pl.UTF-8):	Biblioteka statyczna captury
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static captury library.

%prep
%setup -q -n %{name}-%{version}~svn158.orig

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/captury.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/captury.so

%files static
%defattr(644,root,root,755)
%{_libdir}/captury.a
