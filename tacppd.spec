Summary:	TACACS++ Daemon
Summary(pl):	Serwer TACACS++
Name:		tacppd
Version:	0.0.4
Release:	1
Group:		Networking/Daemons
License:	GPL
Source0:	http://provider.kht.ru/products/tacppd/ftp/unix/tacppd/releases/%{name}-%{version}-src.tgz
Source1:	%{name}.pamd
Source2:	%{name}.initd
Source3:	%{name}.logrotate
URL:		http://provider.kht.ru/products/tacppd/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	ucd-snmp-devel
BuildRequires:	mysql-devel
BuildRequires:	postgresql-devel
Prereq:		/sbin/chkconfig

%description
This is our attempt to create AAA (authentication,authorization,
accounting) server for network devices with additional features. The
main goal - full database support + integration with billing system +
easy user manipulation.

%description -l pl
Serwer AAA (autentyfikacja, autoryzacja, accounting) dla urz±dzeñ
sieciowych plus dodatkowe mo¿liwo¶ci. G³ównym celem jest pe³ne
wsparcie dla baz danych, integracja z systemem bilingowym oraz ³atwa
modyfikacja u¿ytkowników.

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

gzip -9nf BUGS CHANGES COPYING DEVELOPERS FAQ README Release* \
	SNMP* TIP TODO
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
