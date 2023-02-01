#
# Note: this project is no longer maintained. Its developers moved to
# freeradius-client, which, while it hasn't seen a release since 2008,
# contains (a) newer code and (b) is part of an actively maintained
# project that accepts patches, so it might see a release in the
# future. Unfortunately, while opensips supports freeradius-client,
# asterisk doesn't, so it doesn't make much sense to switch. At least
# not yet.
#
Summary:	Radiusclient library and tools
Summary(pl.UTF-8):	Biblioteka radiusclient oraz narzędzia
Name:		radiusclient-ng
Version:	0.5.6
Release:	3
License:	BSD-like
Group:		Libraries
Source0:	http://download.berlios.de/radiusclient-ng/%{name}-%{version}.tar.gz
# Source0-md5:	6fb7d4d0aefafaee7385831ac46a8e9c
Patch0:		%{name}-link.patch
URL:		http://developer.berlios.de/projects/radiusclient-ng/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Radiusclient is a /bin/login replacement which gets called by a getty
to log in a user and to setup the user's login environment. Normal
login programs just check the login name and password which the user
entered against the local password file (/etc/passwd, /etc/shadow). In
contrast to that Radiusclient also uses the RADIUS protocol to
authenticate the user.

%description -l pl.UTF-8
Radiusclient jest zamiennikiem /bin/login wywoływanym przez getty w
celu umożliwienia użytkownikowi zalogowania się. Normalne programy
typu login sprawdzają nazwę użytkownika oraz hasło względem lokalnego
pliku (/etc/passwd, /etc/shadow). W przeciwieństwie do nich
Radiusclient używa także protokołu RADIUS w celu uwierzytelnienia
użytkownika.

%package libs
Summary:	Radius client implementation
Summary(pl.UTF-8):	Implementacja klienta radius
Group:		Libraries
Conflicts:	radiusclient-ng < 0.5.5-2

%description libs
Radius client implementation library.

%description libs -l pl.UTF-8
Biblioteka implementująca klienta protokołu Radius.

%package devel
Summary:	Header files for radiusclient-ng library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki radiusclient-ng
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for radiusclient library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki radiusclient.

%package static
Summary:	Radiusclient static library
Summary(pl.UTF-8):	Statyczna biblioteka radiusclient
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Radiusclient static library.

%description static -l pl.UTF-8
Statyczna biblioteka Radiusclient.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-scp \
	--enable-shadow
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES COPYRIGHT README* doc/*.html
%attr(755,root,root) %{_sbindir}/login.radius
%attr(755,root,root) %{_sbindir}/radacct
%attr(755,root,root) %{_sbindir}/radexample
%attr(755,root,root) %{_sbindir}/radiusclient
%attr(755,root,root) %{_sbindir}/radlogin
%attr(755,root,root) %{_sbindir}/radstatus

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libradiusclient-ng.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libradiusclient-ng.so.2
%attr(750,root,root) %dir %{_sysconfdir}/radiusclient-ng
%attr(640,root,root) %config(missingok,noreplace) %verify(not md5 mtime size) %{_sysconfdir}/radiusclient-ng/dictionary
%attr(640,root,root) %config(missingok,noreplace) %verify(not md5 mtime size) %{_sysconfdir}/radiusclient-ng/dictionary.ascend
%attr(640,root,root) %config(missingok,noreplace) %verify(not md5 mtime size) %{_sysconfdir}/radiusclient-ng/dictionary.compat
%attr(640,root,root) %config(missingok,noreplace) %verify(not md5 mtime size) %{_sysconfdir}/radiusclient-ng/dictionary.merit
%attr(640,root,root) %config(missingok,noreplace) %verify(not md5 mtime size) %{_sysconfdir}/radiusclient-ng/dictionary.sip
%attr(640,root,root) %config(missingok,noreplace) %verify(not md5 mtime size) %{_sysconfdir}/radiusclient-ng/issue
%attr(640,root,root) %config(missingok,noreplace) %verify(not md5 mtime size) %{_sysconfdir}/radiusclient-ng/port-id-map
%attr(640,root,root) %config(missingok,noreplace) %verify(not md5 mtime size) %{_sysconfdir}/radiusclient-ng/radiusclient.conf
%attr(640,root,root) %config(missingok,noreplace) %verify(not md5 mtime size) %{_sysconfdir}/radiusclient-ng/servers

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libradiusclient-ng.so
%{_libdir}/libradiusclient-ng.la
%{_includedir}/radiusclient-ng.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libradiusclient-ng.a
