%{?scl:%scl_package nodejs-buffer-shims}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global npm_name buffer-shims

Name:       %{?scl_prefix}nodejs-%{npm_name}
Version:    1.0.0
Release:    3%{?dist}
Summary:    Some shims for node buffers
License:    MIT
URL:        https://github.com/calvinmetcalf/buffer-shims/issues
Source0:    http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
Some shims for node buffers

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
# If any binaries are included, symlink them to bindir here


%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
#not running tests in RHSCL
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc license.md
%doc readme.md

%changelog
* Mon Jul 03 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-3
- rh-nodejs8 rebuild

* Tue Sep 20 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-2
- Initial build

