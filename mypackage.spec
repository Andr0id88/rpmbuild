Name:           mypackage
Version:        1.0
Release:        1%{?dist}
Summary:        My Simple Package

License:        MIT
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

%description
A simple shell script that prints "Hello from MyPackage!"

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/local/bin
install -m 755 src/mypackage.sh %{buildroot}/usr/local/bin/mypackage

%files
/usr/local/bin/mypackage

%changelog
* Fri Sep 27 2024 Andre Hansen <you@example.com> - 1.0-1
- Initial package

