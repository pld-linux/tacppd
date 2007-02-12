Summary:	TACACS++ Daemon
Summary(pl.UTF-8):   Serwer TACACS++
Name:		tacppd
Version:	0.0.4
Release:	1.1
License:	BSD-like
Group:		Networking/Daemons
# new releases: http://dl.sourceforge.net/tacppd/
Source0:	http://tacppd.org/public-ftp/releases/%{version}/%{name}-%{version}-src.tgz
# Source0-md5:	ca35c0fc3caf9de13a9b55483212e0e3
Source1:	%{name}.pamd
Source2:	%{name}.initd
Source3:	%{name}.logrotate
URL:		http://tacppd.org/
BuildRequires:	mysql-devel
BuildRequires:	postgresql-devel
BuildRequires:	ucd-snmp-devel >= 4.2.5
PreReq:		rc-scripts
#Requires(post,preun):	/sbin/chkconfig
Requires:	pam >= 0.77.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is our attempt to create AAA (authentication,authorization,
accounting) server for network devices with additional features. The
main goal - full database support + integration with billing system +
easy user manipulation.

%description -l pl.UTF-8
Serwer AAA (autentyfikacja, autoryzacja, accounting) dla urządzeń
sieciowych plus dodatkowe możliwości. Głównym celem jest pełne
wsparcie dla baz danych, integracja z systemem bilingowym oraz łatwa
modyfikacja użytkowników.

%prep
%setup -q -n %{name}

%build
cd config
%configure2_13 \
	--with-mysql \
	--with-pgsql
cd ..
%{__make}
%{__make} dbmodules
%{__make} snmpmodules

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES COPYING DEVELOPERS FAQ README Release* SNMP* TIP TODO
