Summary:	TACACS++ Daemon
Summary(pl):	Serwer TACACS++
Name:		tacppd
Version:	0.0.4
Release:	0.1
License:	GPL
Group:		Networking/Daemons
Source0:	http://provider.kht.ru/products/tacppd/ftp/unix/tacppd/releases/%{name}-%{version}-src.tgz
Source1:	%{name}.pamd
Source2:	%{name}.initd
Source3:	%{name}.logrotate
URL:		http://provider.kht.ru/products/tacppd/
BuildRequires:	mysql-devel
BuildRequires:	postgresql-devel
BuildRequires:	ucd-snmp-devel >= 4.2.5
Prereq:		/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is our attempt to create AAA (authentication,authorization,
accounting) server for network devices with additional features. The
main goal - full database support + integration with billing system +
easy user manipulation.

%description -l pl
Serwer AAA (autentyfikacja, autoryzacja, accounting) dla urz�dze�
sieciowych plus dodatkowe mo�liwo�ci. G��wnym celem jest pe�ne
wsparcie dla baz danych, integracja z systemem bilingowym oraz �atwa
modyfikacja u�ytkownik�w.

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
