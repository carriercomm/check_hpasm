%define debug_package %{nil}

Summary:	Nagios plugins to check Hardware Status of HP Proliant and Blades
Name:		check_hpasm
Version:	4.6.2.1
Release:	1%{?dist}
License:	GPLv2+
Group:		Applications/System
URL:		http://labs.consol.de/lang/en/nagios/check_hpasm/
Source0:	http://labs.consol.de/download/shinken-nagios-plugins/check_hpasm-%{version}.tar.gz
Requires:	perl-Nagios-Plugin
BuildRequires:	automake
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
check_hpasm is a Nagio plugin to check the health status of HP Hardware such as 
Proliant And Blade Chassis.

%prep
%setup -T -b0 

%build
aclocal
autoconf
automake
./configure --libexecdir=%{_libdir}/nagios/plugins/ --libdir=%{_libdir}
make 


%install
make install DESTDIR="%{buildroot}"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README COPYING
%{_libdir}/nagios/plugins/check_hpasm

%changelog
* Thu Nov 13 2012 Pall Sigurdsson <palli@opensource.is> 4.6.2.1-1
- Initial packaging
